n,k = map(int, input().split())
s = str(input())
count = 0
for i in range(n):
    if count == k - 1:
        print(s[k - 1].lower(),end = "")
        count += 1
    else:
        print(s[count],end = "")
        count += 1