sx,sy,tx,ty = map(int,input().split())

short_outward = []
short_return = []
long_outward = ["L"]
long_return = ["R"]

for i in range((ty-sy)):
    short_outward.append("U")

for i in range((tx-sx)):
    short_outward.append("R")


for i in range((ty-sy)):
    short_return.append("D")

for i in range((tx-sx)):
    short_return.append("L")


for i in range((ty-sy)+1):
    long_outward.append("U")

for i in range((tx-sx)+1):
    long_outward.append("R")

long_outward.append("D")



for i in range((ty-sy)+1):
    long_return.append("D")

for i in range((tx-sx)+1):
    long_return.append("L")

long_return.append("U")



list = short_outward+short_return+long_outward+long_return

for i in range(len(list)):
    print(list[i],end="")
