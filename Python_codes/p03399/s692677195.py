ABCD = []
for i in range(2):
    ticket = int(input())
    hodai = int(input())
    ABCD.append(min(ticket, hodai))

print(sum(ABCD))
