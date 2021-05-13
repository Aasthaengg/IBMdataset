time = int(input())
h = time//3600
time -= h*3600
m = time//60
time -= m*60
print(str(h)+':'+str(m)+':'+str(time))

