N = int(input())
S = input()

def is_include(t: str, S: str) -> bool:
    tlis = list(t)
    slis = list(S)
    pointer = 0
    len_t = len(tlis)
    for s in slis:
        if s == tlis[pointer]:
            pointer += 1
        if pointer == len_t:
            return True
    return False

cnt = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            t = str(i)+str(j)+str(k)
            if is_include(t, S):
                cnt += 1

print(cnt)
