S = input()
print ':'.join(map(str,[S/3600 ,S%3600/60, S%3600%60]))