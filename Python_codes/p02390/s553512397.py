print(':'.join(map(str, (lambda a: (a // 3600, a // 60 % 60, a % 60))(int(input())))))