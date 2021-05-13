ts = input()
ts = int(ts)
h = int(ts/3600)
ts-= h*3600
m = int(ts/60)
ts -= m*60
text = str(h)+":"+str(m)+":"+str(ts)
print(text)
