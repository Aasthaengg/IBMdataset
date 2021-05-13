v = list(map(int, input()))
for i in range(len(v) - 1):
    if v[i] == v[i+1]:
        print("Bad")
        quit()
print("Good")