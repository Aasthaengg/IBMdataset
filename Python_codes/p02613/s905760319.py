n = int(input())
List = []
for _ in range(n):
    s = str(input())
    List.append(s)
print("AC x", List.count("AC"))
print("WA x", List.count("WA"))
print("TLE x", List.count("TLE"))
print("RE x", List.count("RE"))