def solve():
    def backtrack(nums, cur_state, permutations):
        if not nums:
            permutations[' '.join(cur_state)] = len(permutations)
        for i in range(len(nums)):
            cur_state.append(nums[i])
            backtrack(nums[:i]+nums[i+1:], cur_state, permutations)
            cur_state.pop()

    num = int(input())
    P = str(input())
    Q = str(input())
    # print(num, P, Q)
    nums = [str(i) for i in list(range(1, num+1))]
    permutations = {}
    backtrack(nums, [], permutations)
    # print(permutations)
    print(abs(permutations[Q]-permutations[P]))


if __name__ == "__main__":
    solve()