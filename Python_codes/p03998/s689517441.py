s = {}
s["a"] = list(input())
s["b"] = list(input())
s["c"] = list(input())

turn = "a"
while len(s[turn]) > 0:
    turn = s[turn].pop(0)

print(turn.upper())
