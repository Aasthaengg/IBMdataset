def add(a, b):
    mod = 1e9+7
    c = a + b
    if c >= mod:
        c -= mod
    return c

H, W = [int(x) for x in input().split()]

sl = [input() for _ in range(H)]

dp = [[0 for _ in range(W)] for _ in range(H)]

dp[0][0] = 1 

for i in range(H):
    for j in range(W):
        for frm in [[i-1, j], [i, j-1]]:
            r, c = frm
            if r >= 0 and c >= 0 and sl[r][c] != '#':
                dp[i][j] = add(dp[i][j], dp[r][c])

print(int(dp[H-1][W-1]))


"""
using ll = long long; 
int add(int a, int b) {
    int MOD = 1e9 + 7;
    return (a + b) % MOD;
}
int main() {
    int H;
    int W;
    scanf("%d%d\n", &H, &W);
    vector<vector<int>> dp(H, vector<int>(W));
    vector<vector<bool>> is_wall(H, vector<bool>(W));
    for (int i = 0; i < H; i++) {
        scanf("\n");
        for (int j = 0; j < W; j++) {
            char ch;
            scanf("%c", &ch);
            //cout << i << " " << j << " " << ch << endl;
            if (ch == '#') {
                is_wall[i][j] = true;
            }
        }
    }
    dp[0][0] = 1;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            //cout << i << " " << j << " " << is_wall[i][j] << endl;
            if (!is_wall[i][j]) {
                if (i - 1 >= 0) {
                    dp[i][j] = add(dp[i][j], dp[i-1][j]);
                }
                if (j - 1 >= 0) {
                    dp[i][j] = add(dp[i][j], dp[i][j-1]);
                }    
            }
        }
    }    
	printf("%d\n", dp[H-1][W-1]);
	return 0;
}



"""