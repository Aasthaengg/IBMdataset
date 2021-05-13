n = int(input())
documents = list(map(int, input().split()))

i = 0
for document in documents:
    if document % 2 == 0:
        if not (document % 3 == 0 or document % 5 == 0):
            i = i + 1

if 1 <= i:
    print("DENIED")
else:
    print("APPROVED")
