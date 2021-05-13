S = input()

front = int(S[:2])
rear = int(S[2:])

if (front > 12 and rear > 12) or (front > 12 and rear == 0) or (rear > 12 and front == 0) or (front == 0 and rear == 0):
    print("NA")
    exit()
elif 0 < rear <= 12 and (front > 12 or front == 0):
    print("YYMM")
    exit()
elif 0 < front <= 12 and (rear > 12 or rear == 0):
    print("MMYY")
elif 0 < front <= 12 and 0 < rear <= 12:
    print("AMBIGUOUS")
