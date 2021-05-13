#159_B
def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True

s = input()
n = len(s)

ans = False
if is_kaibun(s):
    s = s[:n//2]
    if is_kaibun(s):
        ans = True
        
if ans:
    print('Yes')
else:
    print('No')