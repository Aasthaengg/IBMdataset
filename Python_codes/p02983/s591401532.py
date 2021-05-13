L, R = map(int, input().split())
min_mod = 2019

if R - L >= 2019:
    for i in range(2018):
        for j in range(i+1, 2019):
            min_mod = min(min_mod, (i*j) % 2019)

else:
    for i in range(L, R):
        for j in range(i+1, R+1):
            min_mod = min(min_mod, (i*j) % 2019)

print(min_mod)
