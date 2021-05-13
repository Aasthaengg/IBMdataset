N = int(input())
count = 0
BA = 0
Ba = 0
bA = 0
for i in range(N):
    a = input()
    count += a.count('AB')
    if a[0] == 'B':
        if a[-1] =='A':
            BA += 1
        else:
            Ba += 1
    elif a[-1] == 'A':
        bA +=1
if BA == 0:
    count += min(Ba,bA)
else:
    if bA or Ba:
        count += BA + min(bA,Ba)
    else:
        count += BA-1
print(count)