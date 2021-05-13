N = input()
n = list(map(int,raw_input().split()))
print(" ".join(list(map(str,n))))
for i in range(1,int(N)):
    v = n[i]
    j = i - 1
    while j >= 0 and v < n[j]:
        n[j+1] = n[j]
        j = j - 1
    n[j+1] = v
    print(" ".join(list(map(str,n))))