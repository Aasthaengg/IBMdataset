l = input()

ans = 1
mod = 10**9+7
strict = 1
# st_m = 0
easy = 0
# ea_m = 0
for i in range(len(l)):
    if l[i] == "1":
        easy *= 3
        easy %= mod

        easy = easy + strict
        # ea_m += st_m
        strict *= 2
        # st_m *= 2
        # st_m += strict//mod
        strict %= mod

    else:
        easy *= 3
        # ea_m *= 3
        # ea_m += easy//mod
        easy %= mod
    # print(easy,strict)

# print(easy,strict)

print((easy+strict)%mod)