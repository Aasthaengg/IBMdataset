temparr = input()
temparr = temparr.split()
k = int(temparr[0])
n = int(temparr[1])
arr = []
temparr = input()
temparr = temparr.split()
for i in temparr:
    arr.append(int(i))
dp = [0 for _ in range(n + 2)]
arr = sorted(arr)
dp[0] = 0 
for i in range(1, n + 2):
    for j in arr:
        if j > i :
            continue 
        if dp[i - j] == 0 :
            dp[i] = 1 
            break 
if dp[n] == 1:
    print("First")
else:
    print("Second")
