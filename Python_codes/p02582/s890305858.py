s = input()

if "RRR" in s:
    print(3)
elif "RR" in s and "S" in s:
    print(2)
elif s.count("R") == 1 or "RSR" in s:
    print(1)
elif s.count("R") == 0:
    print(0)