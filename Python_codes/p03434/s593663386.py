n=int(input())
a=list(map(int, input().split()))
a.sort(reverse=True)
diff=0
for i in range(len(a)):
    if i%2==0: diff += a[i]
    else: diff -= a[i]
print(diff)
