a, b = map(int, input().split())
an = 0
for i in range(a,b+1):
    li = [int(n) for n in str(i)]
    if li[0] == li[4] and li[1] == li[3]:
        an+=1
print(an)