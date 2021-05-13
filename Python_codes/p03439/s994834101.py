n=int(input())
print(n-1)
base=input()
def srh(n,t, str):
    print(((n - 1) // 2) + t)
    point = input()
    if point == 'Vacant':
        return
    if n % 4 == 1:
        if point == str:
            srh((n // 2) + 1, t, point)
        else:
            srh((n // 2) + 1, t + (n // 2), str)
    else:
        if point == str:
            srh(n // 2, t + (n // 2) + 1, str)
        else:
            if point == 'Male':
                srh(n // 2, t, 'Female')
            else:
                srh(n // 2, t, 'Male')
srh(n, 0, base)
