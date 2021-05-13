mazui_med, umai_med, umai_doku = map(int, input().split())

tmp = min(umai_doku, umai_med)
umai_doku -= tmp
umai_med -= tmp
cnt = 2 * tmp

tmp = min(umai_doku, mazui_med)
umai_doku -= tmp
cnt += tmp


if (umai_doku > 0):
    cnt += 1
if (umai_med > 0):
    cnt+=umai_med

print(cnt)