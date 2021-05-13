n = int(input())
mi = n / 1.08
ma = (n+1) / 1.08
tar = int(mi)
while(tar <= ma):
    if mi <= tar < ma:
        print(tar)
        quit()
    tar += 1
print(":(")
