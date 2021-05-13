data = input()
sec = int(data)

h = int(sec / 3600)
sec -= h*3600

m = int(sec / 60)
sec -= m*60

print('{0}:{1}:{2}'.format(h, m, sec))