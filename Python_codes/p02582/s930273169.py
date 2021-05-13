s = input()

if s.count("R")==2 and s[1]=="S":
    print(s.count("R")-1)
else:
    print(s.count("R"))