N = input()[-1]

if N in '24579':
    ans = 'hon'
elif N in '0168':
    ans = 'pon'
elif N == '3':
    ans = 'bon'

print(ans)