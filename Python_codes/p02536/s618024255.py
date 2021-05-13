# There are N cities numbered 1 through N, and M bidirectional roads numbered 1
# through M. Road i connects City A_i and City B_i.
# 
# Snuke can perform the following operation zero or more times:
# 
#  * Choose two distinct cities that are not directly connected by a road, and
#    build a new road between the two cities.
# 
# After he finishes the operations, it must be possible to travel from any city to
# any other cities by following roads (possibly multiple times).
# 
# What is the minimum number of roads he must build to achieve the goal?

# Solution:
#   Use UnionFind to start with groups 1..N and merge as directed by the roads data.
#   If there are G distinct groups after all the merges, then G-1 roads are required
#   to provide the necessary linkages.

class UnionFind:
    # The nodes will be numbered 1..n.
    def __init__(s, n):
        s.n_ = n
        s.ngroups_ = n
        s.parent_  = [i for i in range(n+1)]
          # index zero is ignored

    # Number of nodes.
    def n(s):
        return s.n_

    # Number of distict groups.
    def ngroups(s):
        return s.ngroups_

    # Returns the ultimate parent node of node i, and resets the parent so the chain is
    # shorter for future queries.
    def find(s, i):
        x = i
        while True:
            y = s.parent_[x]
            if x == y:
                # We've found the root of the group.
                s.parent_[i] = x
                return x
            else:
                x = y

    # -> True/False
    def same_group(s, i, j):
        return s.find(i) == s.find(j)

    # Generator of (node_id, group_id) for all nodes.
    def items(s):
        return ((i, s.find(i)) for i in range(1, s.n_ + 1))

    # Merges two groups. Returns True if a merge actually took place, or False if they
    # were in the same group anyway.
    def union(s, i, j):
        x, y = s.find(i), s.find(j)
        if x == y:
            # Same group already.
            return False
        else:
            s.parent_[x] = y
            s.parent_[i] = y
            s.ngroups_ -= 1
            return True

# Read N (number of cities) and M (number of roads).
N, M = [int(x) for x in input().split()]

U = UnionFind(N)

# Process each road and merge groups accordingly.
for _ in range(M):
    a, b = [int(x) for x in input().split()]
    U.union(a, b)

# Get and print the answer.
answer = U.ngroups() - 1
print(answer)
