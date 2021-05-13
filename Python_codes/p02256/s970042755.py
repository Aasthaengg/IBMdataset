def lcd(a,b): ##return least common multiple of a and b
    if a > b:
        return lcd(a-b,b)
    elif a < b:
        return lcd(b-a,a)
    elif a == b:
        return a

a,b = map(int,input().split())
print(lcd(a,b))