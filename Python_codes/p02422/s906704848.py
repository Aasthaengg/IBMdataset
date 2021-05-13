# 9_A
# w = input().upper()
# t = ""
# while True:
#     tmp = input()
#     if tmp == "END_OF_TEXT":
#         break
#     t += tmp.upper() + " "
# list = t.split()
# print(list.count(w))

# 9_B
# while True:
#     t = input()
#     if t == "-":
#         break
#     m = int(input())
#     for i in range(m):
#         h = int(input())
#         t = t[h:] + t[:h]
#     print(t)

# 9_C
# n = int(input())
# score_t, score_h = 0, 0
# for i in range(n):
#     t, h = input().split()
#     if t > h:
#         score_t += 3
#     elif h > t:
#         score_h += 3
#     else:
#         score_t += 1
#         score_h += 1
# print(f"{score_t} {score_h}")

# 9_D
t = str(input())
o_list = []
for i in range(int(input())):
    o_list = input().split()
    a, b = int(o_list[1]), int(o_list[2])
    if o_list[0] == "print":
        print(t[a : b + 1])
    elif o_list[0] == "reverse":
        t = t[:a] + t[a : b + 1][::-1] + t[b + 1 :]
    elif o_list[0] == "replace":
        t = t[:a] + o_list[3] + t[b + 1 :]

