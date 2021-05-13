S = input()

count = S.count("R")
if count == 2 and S[0] == "R" and S[2] == "R":
    count = 1
print(count)