# 092_a
# """
#  あなたは、電車とバスを乗り継いで旅行をする計画を立てました。
#  電車は旅程に沿って通常のきっぷを買うと A円かかり、
#  乗り放題きっぷを買うとB円かかります。
#  バスは旅程に沿って通常のきっぷを買うと C円かかり、
#  乗り放題きっぷを買うと D円かかります。
#
# 電車およびバスについて通常の切符を買うか乗り放題きっぷを買うかをうまく選んだときの、運賃の合計の最小値を求めてください。
# """

A = int(input())
B = int(input())
C = int(input())
D = int(input())
if (1 <= A & A <= 1000) & (1 <= B & B <= 1000) & (1 <= C & C <= 1000) & (1 <= D & D <= 1000):
    print((min(A, B)) + (min(C, D)))
