record = input()

wins = 0

for match in record:
    if(match == "o" or match =="O"):
        wins += 1

matchesPlayed = len(record)

if(15 - matchesPlayed + wins > 7):
    print("YES")
else:
    print("NO")
