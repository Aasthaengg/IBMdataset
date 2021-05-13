a, b =map(int, input().split())
def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True
cnt = 0
for i in range(a, b+1):
    if is_kaibun(str(i)):
        cnt += 1
print(cnt)