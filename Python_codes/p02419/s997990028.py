W = input().casefold()

cnt = 0

while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.casefold()
    words = line.split()
    cnt += words.count(W)
    
print(cnt)