N = int(input())
li = list(map(int, input().split()))
an = (li[0]+li[N-2])
for i in range(1,N-1):
    an+= min(li[i-1],li[i])
print(an)