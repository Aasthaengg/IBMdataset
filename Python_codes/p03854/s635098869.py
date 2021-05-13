S=input()

S = S.replace("dream","w")
S = S.replace("erase","x")
S = S.replace("wer","y")
S = S.replace("xr","z")

if len(S) == S.count("w")+S.count("x")+S.count("y")+S.count("z"):
    print("YES")
else:
    print("NO")
