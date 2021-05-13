def chk_a():
    global a
    for i in range(len(a)):
        if a[i]%2==0:
            a[i]=a[i]//2
        else:
            return False
    return True

n = int(input())
a = list(map(int,input().split()))

for i in range(10**9):
    if chk_a()==False:
        break
print(i)