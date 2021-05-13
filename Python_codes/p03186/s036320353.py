mazui_med, umai_med, umai_doku = map(int, input().split())

N_med = mazui_med + umai_med

if (N_med >= umai_doku):
    ans = umai_med + umai_doku
else:
    ans = umai_med + (mazui_med + umai_med + 1)


print(ans)