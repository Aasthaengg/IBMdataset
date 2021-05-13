N = int(input())
candies_i = list(map(int, input().split()))
candies_j = list(map(int, input().split()))

l = []

for i in range(N):
    total_li = sum(candies_i[:i+1])
    total_lj = sum(candies_j[i:])
    total = total_li + total_lj
    l.append(total)

print(max(l))
