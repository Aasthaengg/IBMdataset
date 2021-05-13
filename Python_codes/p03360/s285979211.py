input_ = [int(s) for s in input().split()]
k = int(input())
input_.sort(key=int)
for _ in range(k):input_[2] *= 2
ans = 0
for i in range(3):ans += input_[i]
print(ans)