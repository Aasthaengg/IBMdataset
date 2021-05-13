# 2019 6/15
# diverta 2019 A Ball Distribution

import sys

ball, human = list(map(int, input().split()))

if human == 1:
    print(0)
    sys.exit()
elif ball >= human:
    print(ball - human)
    sys.exit()