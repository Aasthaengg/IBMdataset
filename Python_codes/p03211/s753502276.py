N = str(input())
mn = 10**10
for i in range(len(N)-2):
    ref = abs(int(N[i:i+3])-753)
    if ref < mn:
        mn = ref
print(mn)