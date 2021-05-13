N = input()


if int(N[-1]) in [2,4,5,7,9]:
    ans = 'hon'
elif int(N[-1]) in [0,6,1,8]:
    ans = 'pon'
else:
    ans = 'bon'

print(ans)
