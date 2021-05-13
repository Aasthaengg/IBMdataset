def pencil_unit(N):
    _ = N % 10
    if _ == 3:
        return 'bon'
    elif _ in [0,1,6,8]:
        return 'pon'
    else:
        return 'hon'

N = int(input())
print(pencil_unit(N))