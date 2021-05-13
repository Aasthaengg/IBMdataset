a, b = map(int, input().split())
def isr(si):
    for j in range(0, len(si)//2):
        if si[j] != si[-1-j]:
            return False
    return True

c = 0
for i in range(a, b+1):
    si = str(i)
    if isr(si):
        c += 1
print(c)