N = int(input())
nums = [  list(map(int,input().split(" "))) for _ in range(N) ]

for i in range(N):
    a,b = nums[i]
    nums[i].append(a + b)
nums =sorted(nums,key = lambda x:-x[2])

takahasi = [nums[i][0] for i  in  range(N) if i % 2 == 0]
aokis= [nums[i][1] for i  in  range(N) if i % 2 != 0]
print(sum(takahasi) - sum(aokis))