#ABC 141
S =input()
W =["Sunny", "Cloudy", "Rainy"]
for i,w in enumerate(W):
    if w==S:
        print(W[(i+1)%3])
        exit()