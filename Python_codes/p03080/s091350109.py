people = int(input())
cap = input()
red = cap.count("R")
if red>(people-red):
    print("Yes")
else:
    print("No")