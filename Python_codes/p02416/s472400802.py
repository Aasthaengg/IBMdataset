while True:
    s=input()
    if s == '0':
        break
    print(str(sum(map(int, s))))