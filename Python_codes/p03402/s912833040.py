g_0 = [["#"]*100 for _ in range(50)]
g_1 = [["."]*100 for _ in range(50)]

a,b = map(int, input().split())
print("100 100")
for i in range(a-1):
    g_0[2*(i//49) + 1][2*(i%49) +1] = "."

for i in range(b-1):
    g_1[2*(i//49) + 1][2*(i%49) +1] = "#"

for i in range(50):
    print("".join(g_0[i]))
for i in range(50):
    print("".join(g_1[i]))



